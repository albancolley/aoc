from sys import argv
import pathlib
from time import now

struct Aoc202301():

    var digits : String
    var word_digits :DynamicVector[String]

    fn __init__(inout self) raises:
        self.digits = '123456789'
        let word_str: String = "one-two-three-four-five-six-seven-eight-nine"
        self.word_digits = word_str.split('-')


    fn calc_1(self, data: DynamicVector[String]) -> Int:
        var total: Int = 0

        for line_idx in range(len(data)):
            var done: Bool = False
            let line = data[line_idx]
            var i: Int = 0
            while i < len(line) and not done:
                var j: Int = 0
                while j < len(self.digits) and not done:
                    if line[i] == self.digits[j]: 
                        done = True
                        try:
                            total += atol(line[i])*10
                        except e:
                            print(e)
                    j += 1
                i += 1

            done = False
            i = len(line) - 1
            while i >= 0 and not done:
                var j: Int = 0
                while j < len(self.digits) and not done:
                    if line[i] == self.digits[j]: 
                        done = True
                        try:
                            total += atol(line[i])*1
                        except e:
                            print(e)
                    j += 1
                i -= 1

        return total


    fn calc_2(self, data: DynamicVector[String]) -> Int:
        var total: Int = 0

        for line_idx in range(len(data)):
            var done: Bool = False
            let line = data[line_idx]
            var i: Int = 0
            while i < len(line) and not done:
                var j: Int = 0
                while j < len(self.digits) and not done:
                    if line[i] == self.digits[j]: 
                        done = True
                        try:
                            total += atol(line[i])*10
                        except e:
                            print(e)
                    j += 1
                    
                j  = 0
                while j < len(self.word_digits) and not done:
                    let word:String = self.word_digits[j]
                    if line[i:i+len(word)] == word: 
                        done = True
                        try:
                            total += atol(self.digits[j])*10
                        except e:
                            print(e)
                    j += 1
                i += 1

            done = False
            i = len(line) - 1
            while i >= 0 and not done:
                var j: Int = 0
                while j < len(self.digits) and not done:
                    if line[i] == self.digits[j]: 
                        done = True
                        try:
                            total += atol(line[i])*1
                        except e:
                            print(e)
                    j += 1
                j = 0
                while j < len(self.word_digits) and not done:
                    let word:String = self.word_digits[j]
                    if line[i:i+len(word)] == word: 
                        done = True
                        try:
                            total += atol(self.digits[j])*1
                        except e:
                            print(e)
                    j += 1
                i -= 1

        return total

    fn load_handler_part1(self, data:DynamicVector[String]) -> DynamicVector[String]:
        return data

    fn load_handler_part2(self, data:DynamicVector[String]) -> DynamicVector[String]:
        return data

fn main() raises: 
    let start_time:Int = now()

    let a:Aoc202301 = Aoc202301()

    let path_str: String = argv()[0]
    
    let last_path = path_str.rfind(pathlib.path.DIR_SEPARATOR)

    var part1_filenames:DynamicVector[String] = DynamicVector[String]()
    part1_filenames.append("part1_1.txt")
    part1_filenames.append("part1_2.txt")
    
    var part2_filenames:DynamicVector[String] = DynamicVector[String]()
    part2_filenames.append("part2_1.txt")
    part2_filenames.append("part2_2.txt")

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
        let data:DynamicVector[String] = a.load_handler_part1(rows)
        print(a.calc_1(data))

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

        let data:DynamicVector[String] = a.load_handler_part2(rows)
        print(a.calc_2(data))

    let end_time:Int = now()

    print_no_newline("Total time ")
    print_no_newline((end_time - start_time)/1000000000.0)
    print("s")
