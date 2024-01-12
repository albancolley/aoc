# import os.path
# import string

# from aoc2022.common.aocbase import AocBase
# from aoc2022.common.setup import configure
# import logging

# from PIL import Image, ImageColor



# def calc_1(data ) -> Int:
#     count = 0
#     cave, max_y, min_x, max_x = data
#     sand_pos_x = 500
#     sand_pos_y = 0
#     pos = None
#     draw(count, cave, (1 + (max_x - min_x), max_y + 1), min_x, pos)
#     while True:
#         pos = (sand_pos_x, sand_pos_y)
#         below = (sand_pos_x, sand_pos_y+1)
#         left = (sand_pos_x-1, sand_pos_y+1)
#         right = (sand_pos_x+1, sand_pos_y+1)
#         if below in cave:
#             if left in cave and right in cave:
#                 cave[pos] = "o"
#                 draw(count, cave, (1 + (max_x - min_x), max_y + 1), min_x, pos)
#                 count += 1
#                 sand_pos_x = 500
#                 sand_pos_y = 0
#                 continue
#             if left not in cave:
#                 sand_pos_x -= 1
#                 sand_pos_y += 1
#             elif right not in cave:
#                 sand_pos_x += 1
#                 sand_pos_y += 1
#         else:
#             sand_pos_y += 1
#         if max_y < sand_pos_y:
#             break
#     draw(count, cave, (1 + (max_x - min_x), max_y + 1), min_x, None)
#     return count

# def calc_2(data: [str]) -> int:
#     count = 0
#     cave, max_y, min_x, max_x = data
#     sand_pos_x = 500
#     sand_pos_y = 0
#     pos = None
#     extra = 200
#     size = (extra*2 + (max_x - min_x), max_y + 4)
#     draw(count, cave, size, min_x, pos, extra)
#     while True:
#         pos = (sand_pos_x, sand_pos_y)
#         below = (sand_pos_x, sand_pos_y + 1)
#         left = (sand_pos_x - 1, sand_pos_y + 1)
#         right = (sand_pos_x + 1, sand_pos_y + 1)
#         if below in cave:
#             if left in cave and right in cave:

#                 cave[pos] = "o"
#                 if count % 100 == 0:
#                     draw(count, cave, size, min_x, pos, extra)
#                 count += 1
#                 sand_pos_x = 500
#                 sand_pos_y = 0
#                 if (500, 0) == pos:
#                     break
#                 continue
#             if left not in cave:
#                 sand_pos_x -= 1
#                 sand_pos_y += 1
#             elif right not in cave:
#                 sand_pos_x += 1
#                 sand_pos_y += 1
#         else:
#             sand_pos_y += 1
#         # min_x = min(min_x, sand_pos_x)
#         # max_x = max(max_x, sand_pos_x)
#         if max_y + 2 == sand_pos_y:
#             new_pos_above = (sand_pos_x, sand_pos_y-1)
#             cave[new_pos_above] = "o"
#             cave[(sand_pos_x, sand_pos_y)] = "#"
#             if count % 100 == 0:
#                 draw(count, cave, size, min_x, pos, extra)
#             count += 1
#             sand_pos_x = 500
#             sand_pos_y = 0
#     draw(count, cave, size, min_x, None, extra)
#     return count

# def load_handler_part1(data: [str]) -> {}:
#     cave = {}
#     max_y = 0
#     min_x = 2000000
#     max_x = 0
#     for path in data:
#         points = path.split(' -> ')
#         last_coord = points[0].split(',')
#         for point in points[1:]:
#             coord = point.split(',')
#             x1 = min(int(last_coord[0]), int(coord[0]))
#             x2 = max(int(last_coord[0]), int(coord[0]))
#             y1 = min(int(last_coord[1]), int(coord[1]))
#             y2 = max(int(last_coord[1]), int(coord[1]))
#             max_y = max(max_y, y2)
#             min_x = min(min_x, x1)
#             max_x = max(max_x, x2)
#             for x in range(x1, x2+1):
#                 for y in range(y1, y2+1):
#                     cave[(x, y)] = '#'
#             last_coord = coord
#     return cave, max_y, min_x, max_x


# def load_handler_part2(data: [str]) -> [str]:
#     return load_handler_part1(data)


# def splitext(filename: String) -> String
#     pring(filename.splitext())
#     return filename.splitext()


# def draw(count, cave, size, min_x, last_sand, extra=0):
#     pass
#     # image = Image.new("RGB", size, color= ImageColor.getrgb('white'))
#     # source = (500 - min_x + extra, 0)
#     # image.putpixel(source, ImageColor.getrgb('blue'))
#     # for key in cave:
#     #     value = cave[key]
#     #     if value == "#":
#     #         colour = ImageColor.getrgb('black')
#     #     elif value == "o":
#     #         colour = ImageColor.getrgb('yellow')
#     #     key = (key[0] - min_x, key[1])
#     #     x, y = key
#     #     x = x + extra
#     #     if 0 <= x < size[0] and 0 <= y < size[1]:
#     #         image.putpixel((x, y), colour)
#     # if last_sand:
#     #     if 0 <= x < size[0] and 0 <= y < size[1]:
#     #         image.putpixel((x,y), ImageColor.getrgb('red'))
#     # path = os.path.join('C:\\WIP\\aoc', f'{count:06}.png')
#     # # (width, height) = (image.width * 2, image.height * 2)
#     # # i2 = image.resize((width, height), Image.Resampling.BOX )
#     # image.save(path)


# struct Results:
#     var filename: String
#     var valid: Bool
#     var expected: Int
#     var result: Int
#     var load_time: Int
#     var calc_time: Int

#     fn __init__(inout self, filename: Int, valid: Bool, expected: Int, result: Int, load_time: Int, calc_time: Int):
#         self.filename = filename
#         self.valid = valid
#         self.expected = expected
#         self.result = result
#         self.load_time = load_time
#         self.calc_time = calc_time
    

# def part_1(filename: str) -> Results:
#     start_time = time.perf_counter()
#     data = load_file(filename, load_handler_part1)
#     load_time = time.perf_counter()
#     result = calc_1(data)
#     calc_time = time.perf_counter()

#     split_filename = splitext(filename)
#     expected_filename = "./" + split_filename[0] + "_result" + split_filename[1]
#     try:
#         var f = open(expected_filename, 'r') 
#         f.close()
#     except:
#         with open(expected_filename, 'w') as f:
#             print(-1, file=f)
#     expected = load_file(expected_filename)[0]
#     success = False
#     try:
#         expected = type(result)(load_file(expected_filename)[0])
#         success = expected == result
#     except ValueError:
#         success = False
   
#     r = Results(filename, expected == result, expected, result, load_time - start_time, calc_time - load_time )
#     return r


#     def part_2(filename: String) -> Results:
#         var start_time = time.perf_counter()
#         var data = load_file(filename, load_handler_part2)
#         var load_time = time.perf_counter()
#         var result = calc_2(data)
#         var calc_time = time.perf_counter()

#         var split_filename = splitext(filename)
#         var expected_filename = "./" + split_filename[0] + "_result" + split_filename[1]
#         try:
#             var f = open(expected_filename, 'r') 
#             f.close()
#         except:
#             with open(expected_filename, 'w') as f:
#                 print(-1, file=f)
#         expected = type(result)(load_file(expected_filename)[0])
#         r = Results(filename, expected == result, expected, result, load_time - start_time, calc_time - load_time )
#         return r

# def glob_re(pattern, strings):
#     return filter(re.compile(pattern).match, strings)

# def run_part_1(filepath: str) -> []:
#     results = []
#     if filepath is not None and len(filepath) > 0:
#         filenames = glob_re(filepath, os.listdir())
#         for filename in filenames:
#             start = time.perf_counter()
#             result = part_1(filename)
#             took = time.perf_counter() - start
#             results += [result + (took,)]
#     return results

# def run_part_2(filepath: str) -> []:
#     results = []
#     if filepath is not None and len(filepath) > 0:
#         filenames = glob_re(filepath, os.listdir())
#         for filename in filenames:
#             start = time.perf_counter()
#             result = part_2(filename)
#             took = time.perf_counter() - start
#             results += [result + (took,)]
#     return results

fn run(part1_path: String, part2_path: String) -> Bool:
    let results = [[[False]], [[True]]]
    # var results = { "Part 1":run_part_1(part1_path), "Part 2": run_part_2(part2_path)}
    # print(f'{"":21s} {"Expected":30s} {"Actual":30s} {"Time (s.ms)":8s} {"Load Time":8s} {"Calc Time":8s}')
    # display(results, "Part 1")
    # display(results, "Part 2")
    var failed = False
    for i in range(len(results)):
        print(results.get(i))
    # for result in results:
    #      for runs in results:
    #          if not runs[1]:
    #              failed = True
    #              break
    return failed

def display(results, part):
    pass
    # print(f'{part:21s}')
    # for result in results[part]:
    #     star = '*'
    #     if result[1]:
    #         star = ' '
    #     print(f'{star}{result[0]:20s} {str(result[2])[0:30]:30s} {str(result[3])[0:30]:30s} {result[6]:010.6f}  {result[4]:010.6f}  {result[5]:010.6f}')

fn main():
    let failed: Bool = run("part1_[0-9]+.txt", "part2_[0-9]+.txt")
    if failed == False:
        print("failed")
