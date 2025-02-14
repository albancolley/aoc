from sys import argv
import pathlib
from time import now
from collections.dict import Dict, KeyElement, DictEntry
from collections.optional import Optional
from math import round, max
from hashmap import HashMapDict
from fnv1a import fnv1a64

@value
struct Entry(CollectionElement, Stringable):
    var step: Int
    var position: StaticIntTuple[2]  
    var path: String
    var skip: Bool
    
    fn __init__(inout self, step:Int, position:StaticIntTuple[2],  path: String = "", skip:Bool = True):
        self.step = step
        self.position = position
        self.path = path
        self.skip = skip

    fn in_path(self, position:StaticIntTuple[2]) -> Bool:
        return self.path.find(str(position)) < 0

    fn __copyinit__(inout self, existing: Self):
        self.step = existing.step
        self.position = existing.position
        self.skip = existing.skip
        self.path = existing.path

    fn __moveinit__(inout self, owned existing: Self):
        self.step = existing.step
        self.position = existing.position
        self.skip = existing.skip
        self.path = existing.path

    fn __str__(self) -> String:
        return str(self.step) + " " + str(self.position) + self.path

struct Stack:
    var data: DynamicVector[Entry]
    var top : Int
    var size : Int
    
    fn __init__(inout self):
        self.top = -1
        self.size = 16
        self.data = DynamicVector[Entry]()
        
    fn __init__(inout self,stackSize: Int):
        self.top = -1
        self.size = stackSize
        self.data = DynamicVector[Entry]()

    fn push(inout self,value : Entry):
        self.top = self.top + 1
        if self.top < len(self.data):
            self.data[self.top] = value
        else: 
            self.data.append(value)
    
    fn pop(inout self) raises-> Optional[Entry]:
        if self.top == -1:
            return Optional[Entry]()
        let popval = self.data[self.top]
        self.top = self.top - 1
        return Optional[Entry](popval)
    
    fn __del__(owned self):
        self.data.clear()

@value
struct StringKey(KeyElement):
    var s: String

    fn __init__(inout self, owned s: String):
        self.s = s ^

    fn __init__(inout self, s: StringLiteral):
        self.s = String(s)

    fn __hash__(self) -> Int:
        let ptr = self.s._buffer.data.value
        return hash(DTypePointer[DType.int8](ptr), len(self.s))

    fn __eq__(self, other: Self) -> Bool:
        return self.s == other.s


@value
struct Path(CollectionElement, Stringable):
    var start: StaticIntTuple[2]
    var end: StaticIntTuple[2]
    var length: Int

    fn __eq__(self, other: Path) -> Bool:
        if self.start != other.start:
            return False
        if self.end != other.end:
            return False
        if self.length != other.length:
            return False
        return True

    fn __str__(self) -> String:
        return str(self.start) + " " + str(self.end) + " " + self.length

@value
struct Item():
    var previous: Pointer[Self]
    var next: Pointer[Self]
    var entry: Entry


struct LinkedList(Stringable):
    var first: Item
    var last: Item
    var length: Int

    fn __str__(self) -> String:
        return str(self.length)

alias grid_type = DType.int16

struct Grid:
    var grid: DTypePointer[grid_type]
    var width: Int
    var height: Int
    var start: StaticIntTuple[2]
    var end: StaticIntTuple[2]

    # Initialize zeroeing all values
    fn __init__(inout self, width: Int, height: Int, start: StaticIntTuple[2], end: StaticIntTuple[2]):
        self.grid = DTypePointer[grid_type].alloc(width * height)
        memset_zero(self.grid, width * height)
        self.width = width
        self.height = height
        self.start = start
        self.end = end
    
    fn __moveinit__(inout self, owned existing: Self):
        self.width = existing.width
        self.height = existing.height
        self.start = existing.start
        self.end = existing.end
        self.grid = existing.grid

    fn __copyinit__(inout self, existing: Self):
        self.width = existing.width
        self.height = existing.height
        self.start = existing.start
        self.end = existing.end
        self.grid = DTypePointer[grid_type].alloc(self.width * self.height)
        for i in range(self.width * self.height):
            self.grid.store(i, existing.grid.load(i))

    
    fn __getitem__(self, x: Int, y: Int) -> String:
        if x < 0 or x >= self.width:
            return '#'
        if y < 0 or y >= self.height:
            return '#'
        return chr(self.load[1](x, y).to_int())

    fn __getitem__(self, pos: StaticIntTuple[2]) -> String:
        return self.__getitem__(pos[0], pos[1])

    fn __setitem__(self, x: Int, y: Int, val: String):
        return self.store[1](x, y, ord(val[0]))

    fn __setitem__(self, pos: StaticIntTuple[2], val: String):
        return self.store[1](pos[0], pos[1], ord(val[0]))

    fn load[nelts: Int](self, x: Int, y: Int) -> SIMD[grid_type, nelts]:
        return self.grid.simd_load[nelts](y * self.width + x)

    fn store[nelts: Int](self, x: Int, y: Int, val: SIMD[grid_type, nelts]):
        return self.grid.simd_store[nelts](y * self.width + x, val)    

    fn dump(self):
        print_no_newline("W:")
        print_no_newline(self.width)
        print_no_newline(" H:")
        print_no_newline(self.height)
        print_no_newline(" S:")
        print_no_newline(self.start)
        print_no_newline(" E:")
        print_no_newline(self.end)
        print()
        for y in range(self.height):
            for x in range(self.width):
                print_no_newline(self[x, y])
            print()
        print()



struct Aoc202323():
    var moves: Dict[StringKey, DynamicVector[Tuple[Int, Int]]]

    fn __init__(inout self):
        self.moves = Dict[StringKey, DynamicVector[Tuple[Int, Int]]]()
        var a:DynamicVector[Tuple[Int, Int]] =  DynamicVector[Tuple[Int, Int]]()
        a.append((0,1))
        a.append((0,-1))
        a.append((1,0))
        a.append((-1,0))
        self.moves['.'] = a
        var a1 =  DynamicVector[Tuple[Int, Int]]()
        a1.append((1, 0))
        self.moves['>'] = a1
        var a2 =  DynamicVector[Tuple[Int, Int]]()
        a2.append((-1, 0))
        self.moves['<'] = a2
        var a3 =  DynamicVector[Tuple[Int, Int]]()
        a3.append((0, -1))
        self.moves['^'] = a3
        var a4 =  DynamicVector[Tuple[Int, Int]]()
        a4.append((0, 1))
        self.moves['v'] = a4

    fn dfs1(self, grid: Grid) raises -> Int:

        var seen: Dict[StringKey, Int] = Dict[StringKey, Int]()

        var queue: DynamicVector[Entry] = DynamicVector[Entry]()
        queue.append(Entry(0, grid.start))

        while len(queue) > 0:
            let entry: Entry = queue.pop_back()
            let tile:String = grid[entry.position]
            let next_step:Int = entry.step + 1
            for i in range(len(self.moves[tile])):
                let move: Tuple[Int, Int] = self.moves[tile][i]
                let next_position: StaticIntTuple[2] = (entry.position[0] + move.get[0, Int](), entry.position[1] + move.get[1, Int]())

                if grid[next_position[0], next_position[1]] == '#':
                    continue

                if entry.path.find(next_position) >= 0:
                    continue

                var seen_next: Optional[Int] = seen.find(str(next_position))
                var value:Int = 0
                if seen_next:
                   value = seen_next.value() 

                if value < next_step:
                    seen[str(next_position)] = next_step
                    var new_path:String = entry.path + " " + str(next_position)
                    queue.push_back(Entry(next_step, next_position, new_path))
        
        return seen[str(grid.end)]
                


    fn dfs(self, grid: Grid, start: StaticIntTuple[2]) raises -> DynamicVector[Path]:

        var queue: DynamicVector[Entry] = DynamicVector[Entry]()
        queue.append(Entry(0, start, str(start)))
        var new_paths:DynamicVector[Path] = DynamicVector[Path]()

        while len(queue) > 0:
            let entry: Entry = queue.pop_back()
            let tile:String = grid[entry.position]
            let next_step:Int = entry.step + 1
            var skip:Bool = entry.skip
            if tile == '<' or tile == '>' or tile =='^' or tile =='v':
                if skip:
                    skip = False
                else:
                    let move: Tuple[Int, Int] = self.moves[tile][0]
                    let next_position: StaticIntTuple[2] = (entry.position[0] + move.get[0, Int](), entry.position[1] + move.get[1, Int]())    
                    var new_path:String = entry.path + " " + str(next_position)
                    new_paths.append(Path(start, next_position, next_step))
                    continue

            for i in range(len(self.moves[tile])):
                let move: Tuple[Int, Int] = self.moves[tile][i]
                let next_position: StaticIntTuple[2] = (entry.position[0] + move.get[0, Int](), entry.position[1] + move.get[1, Int]())

                if grid[next_position[0], next_position[1]] == '#':
                    continue

                if entry.path.find(next_position) >= 0:
                    continue

                var new_path:String = entry.path + " " + str(next_position)
                queue.push_back(Entry(next_step, next_position, new_path, skip))
        
        return new_paths


    fn dfs3(self, entry: Entry, grid: Grid, path: Grid, simple_paths:Dict[StringKey, DynamicVector[Path]]) raises -> Int:
        # print(entry)
        path[entry.position] = 1
        var longest_path:Int = 0
        let simple_path:DynamicVector[Path] = simple_paths[str(entry.position)]
        for i in range(len(simple_path)):
            let next_position:Path = simple_path[i]
            let new_length:Int = entry.step + next_position.length
            if next_position.end == grid.end:
                # print(entry.path, new_length)
                longest_path = max(longest_path, new_length)
            elif path[next_position.end] != 1:
                var next_entry = Entry(new_length, next_position.end, "")
                longest_path = max(self.dfs3(next_entry, grid, path, simple_paths), longest_path)
        path[entry.position] = 0
        return longest_path

    fn dfs32(self, entry: Entry, grid: Grid, path: Grid, simple_paths:HashMapDict[DynamicVector[Path], fnv1a64]) raises -> Int:
        # print(entry)
        path[entry.position] = 1
        var longest_path:Int = 0
        let simple_path:DynamicVector[Path] = simple_paths.get(str(entry.position), DynamicVector[Path]())
        for i in range(len(simple_path)):
            let next_position:Path = simple_path[i]
            let new_length:Int = entry.step + next_position.length
            if next_position.end == grid.end:
                # print(entry.path, new_length)
                longest_path = max(longest_path, new_length)
            elif path[next_position.end] != 1:
                var next_entry = Entry(new_length, next_position.end, "")
                longest_path = max(self.dfs32(next_entry, grid, path, simple_paths), longest_path)
        path[entry.position] = 0
        return longest_path

    fn calc_1(self, grid: Grid) raises -> Int:
        return self.dfs1(grid)

    fn calc_2(self, grid: Grid) raises -> Int:
        grid[grid.start] = 'v'
        grid[grid.end[0], grid.end[1] - 1] = 'v'

        var new_paths: DynamicVector[Path] = self.dfs(grid, grid.start)

        var simple_paths:HashMapDict[DynamicVector[Path], fnv1a64] = HashMapDict[DynamicVector[Path], fnv1a64]()
        while len(new_paths) > 0:
            let path: Path = new_paths.pop_back()
            var found:Bool = False
            var simple_path = simple_paths.get(str(path.start), DynamicVector[Path]())
            for i in range(len(simple_path)):
                if path == simple_path[i]:
                    found = True
                    break
            if not found:
                simple_path.append(path)
            simple_paths.put(str(path.start), simple_path)

            found = False
            let reverse_path:Path = Path(path.end, path.start, path.length)
            var simple_path2 = simple_paths.get(str(reverse_path.start), DynamicVector[Path]())
            for i in range(len(simple_path2)):
                if reverse_path == simple_path2[i]:
                    found = True
                    break
            if not found:
                simple_path2.append(reverse_path)

            simple_paths.put(str(reverse_path.start), simple_path2)

            var paths:DynamicVector[Path] = self.dfs(grid, path.end)
            for i in range(len(paths)):
                new_paths.append(paths[i])


        var path:Grid = Grid(grid.width, grid.height, grid.start, grid.end)
        var longest_path:Int = self.dfs32(Entry(0, grid.start, str(grid.start)),
            grid,
            path,
            simple_paths
        )

        return longest_path

    fn calc_2_old(self, grid: Grid) raises -> Int:
        grid[grid.start] = 'v'
        grid[grid.end[0], grid.end[1] - 1] = 'v'

        var new_paths: DynamicVector[Path] = self.dfs(grid, grid.start)

        var simple_paths:Dict[StringKey, DynamicVector[Path]] =  Dict[StringKey, DynamicVector[Path]]()
        while len(new_paths) > 0:
            let path: Path = new_paths.pop_back()
            if not simple_paths.find(str(path.start)):
                simple_paths[str(path.start)] = DynamicVector[Path]()
            var found:Bool = False
            for i in range(len (simple_paths[str(path.start)])):
                if path == simple_paths[str(path.start)][i]:
                    found = True
                    break
            if not found:
                simple_paths[str(path.start)].append(path)

            if not simple_paths.find(str(path.end)):
                simple_paths[str(path.end)] = DynamicVector[Path]()

            let reverse_path:Path = Path(path.end, path.start, path.length)

            found = False
            for i in range(len (simple_paths[str(path.end)])):
                if reverse_path == simple_paths[str(path.end)][i]:
                    found = True
                    break
            if not found:
                simple_paths[str(path.end)].append(reverse_path)

            var paths:DynamicVector[Path] = self.dfs(grid, path.end)
            for i in range(len(paths)):
                new_paths.append(paths[i])


        var path:Grid = Grid(grid.width, grid.height, grid.start, grid.end)
        var longest_path:Int = self.dfs3(Entry(0, grid.start, str(grid.start)),
            grid,
            path,
            simple_paths
        )

        # var all_paths: DynamicVector[Entry] = DynamicVector[Entry]()
        # all_paths.append(Entry(0, grid.start, str(grid.start)))
        # while len(all_paths) > 0:
        #     let entry:Entry = all_paths.pop_back()
        #     # print(entry)
        #     let simple_path:DynamicVector[Path] = simple_paths[str(entry.position)]
        #     for i in range(len(simple_path)):
        #         let next_position:Path = simple_path[i]
        #         let new_length:Int = entry.step + next_position.length
        #         if next_position.end == grid.end:
        #             if longest_path < new_length:
        #                 longest_path = new_length
        #                 # print(longest_path)
        #         elif entry.in_path(next_position.end):
        #             all_paths.push_back(Entry(new_length, next_position.end, entry.path + str(next_position.end)))

        # var stack:Stack = Stack()
        # stack.push(Entry(0, grid.start, str(grid.start)))
        # while True:
        #     let entry_option:Optional[Entry] = stack.pop()
        #     if not entry_option:
        #         break
        #     let entry:Entry = entry_option.value()
        #     # print(entry)
        #     let simple_path:DynamicVector[Path] = simple_paths[str(entry.position)]
        #     for i in range(len(simple_path)):
        #         let next_position:Path = simple_path[i]
        #         # print(i, next_position)
        #         let new_length:Int = entry.step + next_position.length
        #         if next_position.end == grid.end:
        #             if longest_path < new_length:
        #                 longest_path = new_length
        #                 # print(new_length, entry.path + str(next_position.end))
                    
        #         elif entry.path.find(str(next_position.end)) < 0:
        #             stack.push(Entry(new_length, next_position.end, entry.path + str(next_position.end)))
                   

        return longest_path

    
    fn load_handler_part1(self, data:DynamicVector[String]) -> Grid:
        let width: Int =len(data[0].strip())
        let height: Int = len(data)
        var start: StaticIntTuple[2] = (0, 0)
        var end: StaticIntTuple[2] = (0, 0)
        for col in range(width):
            let tile:String = data[0][col]
            if tile == '.':
                start = (col, 0)
                break

        for col in range(width):
            let tile:String = data[height - 1][col]
            if tile == '.':
                end = (col, (width-1))
                break

        let grid:Grid = Grid(width, height, start, end)
        for y in range(height):
            for x in range(width):
                grid[x, y] = data[y][x]
                
        return grid

    fn load_handler_part2(self, data:DynamicVector[String]) -> Grid:
        return self.load_handler_part1(data)

fn ns_to_ms(ns: Int) -> Int:
    return ((ns/1000000000.0)*1000).to_int()

fn main() raises: 
    let start_time:Int = now()
    let path_str: String = argv()[0]
    
    let last_path = path_str.rfind(pathlib.path.DIR_SEPARATOR)

    var part1_filenames:DynamicVector[String] = DynamicVector[String]()
    part1_filenames.append("part1_1.txt")
    part1_filenames.append("part1_2.txt")

    let aoc202323:Aoc202323 = Aoc202323()

    let file_name_index:Int
    for file_name_index in range(len(part1_filenames)):
        let filename: String = part1_filenames[file_name_index]
        let full_filename: String = path_str[0:last_path+1] + filename

        let input: String
        with open(full_filename, "r") as f:
            input = f.read()

        let rows:DynamicVector[String]
        try:
            rows = input.split('\n')
        except e:
            print('Error')
        let start:Int = now()
        let grid:Grid = aoc202323.load_handler_part1(rows)
        let load_end:Int = now()
        # grid.dump()
        let result: Int = aoc202323.calc_1(grid)
        let end:Int = now()
        print(result, "\ttotal time: " + str(ns_to_ms(end- start)) + "ms", "\tcalc time: " + str(ns_to_ms(end- load_end)) + "ms ", "\tload time: " + str(ns_to_ms(load_end - start)) + "ms")
    
    var part2_filenames:DynamicVector[String] = DynamicVector[String]()
    part2_filenames.append("part2_1.txt")
    part2_filenames.append("part2_2.txt")

    for file_name_index in range(len(part2_filenames)):
        let filename: String = part2_filenames[file_name_index]
        let full_filename: String = path_str[0:last_path+1] + filename

        let input: String
        with open(full_filename, "r") as f:
            input = f.read()

        let rows:DynamicVector[String]
        try:
            rows = input.split('\n')
        except e:
            print('Error')
        let start:Int = now()
        let grid:Grid = aoc202323.load_handler_part2(rows)
        let load_end:Int = now()
        # grid.dump()
        let result: Int = aoc202323.calc_2(grid)
        let end:Int = now()
        print(result, "\ttotal time: " + str(ns_to_ms(end- start)) + "ms", "\tcalc time: " + str(ns_to_ms(end- load_end)) + "ms ", "\tload time: " + str(ns_to_ms(load_end - start)) + "ms")
