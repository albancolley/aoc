import os
import re
import time
from abc import ABCMeta, abstractmethod
from .io import load_file
from os.path import splitext, exists
import logging
from dataclasses import dataclass

logger = logging.getLogger("AOC Base")

@dataclass
class Result:
    filename: str
    success: bool
    expected: str
    actual: str
    load_time: float
    calc_time: float
    overall_time: float = 0

class AocBase(metaclass=ABCMeta):
    @abstractmethod
    def calc_1(self, data: [str]) -> int:
        pass

    @abstractmethod
    def calc_2(self, data: [str]) -> int:
        pass

    @abstractmethod
    def load_handler_part1(self, data: [str]) -> [str]:
        pass

    @abstractmethod
    def load_handler_part2(self, data: [str]) -> [str]:
        pass

    def part_1(self, filename: str) -> Result:
        start_time = time.perf_counter()
        data = load_file(filename, self.load_handler_part1)
        load_time = time.perf_counter()
        result = self.calc_1(data)
        calc_time = time.perf_counter()

        split_filename = splitext(filename)
        expected_filename = split_filename[0] + "_result" + split_filename[1]
        if not exists(expected_filename):
            with open(expected_filename, 'w') as f:
                print(-1, file=f)
        expected = load_file(expected_filename)[0]
        success = False
        try:
            expected = type(result)(load_file(expected_filename)[0])
            success = expected == result
        except ValueError:
            success = False

        result = Result(filename, expected == result, str(expected), str(result)
                        , load_time - start_time, calc_time - load_time)

        return result

    def part_2(self, filename: str) -> Result:
        start_time = time.perf_counter()
        data = load_file(filename, self.load_handler_part2)
        load_time = time.perf_counter()
        result = self.calc_2(data)
        calc_time = time.perf_counter()

        split_filename = splitext(filename)
        expected_filename = split_filename[0] + "_result" + split_filename[1]
        if not exists(expected_filename):
            with open(expected_filename, 'w') as f:
                print(-1, file=f)
        expected = type(result)(load_file(expected_filename)[0])
        result = Result(filename, expected == result, str(expected), str(result)
                        , load_time - start_time, calc_time - load_time)

        return result


    @staticmethod
    def glob_re(pattern, strings):
        return filter(re.compile(pattern).match, strings)

    def run_part_1(self, filepath: str) -> []:
        results = []
        if filepath is not None and len(filepath) > 0:
            filenames = self.glob_re(filepath, os.listdir())
            for filename in filenames:
                start = time.perf_counter()
                result = self.part_1(filename)
                took = time.perf_counter() - start
                result.overall_time = took
                results.append(result)
                self.display(result)
        return results

    def run_part_2(self, filepath: str) -> []:
        results = []
        if filepath is not None and len(filepath) > 0:
            filenames = self.glob_re(filepath, os.listdir())
            for filename in filenames:
                start = time.perf_counter()
                result = self.part_2(filename)
                took = time.perf_counter() - start
                result.overall_time = took
                results.append(result)
                self.display(result)
        return results

    def run(self, part1_path: str, part2_path: str) -> []:
        print(f'{"":21s} {"Expected":30s} {"Actual":30s} {"Time (s.ms)":8s} {"Load Time":8s} {"Calc Time":8s}')
        print(f'{"Part 1":21s}')
        p1 = self.run_part_1(part1_path)
        print(f'{"Part 2":21s}')
        p2 = self.run_part_2(part2_path)
        results = [p1, p2]
        failed = False
        for result in results:
            run: Result
            for run in result:
                if not run.success:
                    failed = True
                    break
        return failed, results

    def display(self, result):
        star = '*'
        if result.success:
            star = ' '
        print(f'{star}{result.filename:20s} {result.expected[0:30]:30s} '
              f'{result.actual[0:30]:30s} {result.overall_time:010.6f}'
              f'  {result.load_time:010.6f}  {result.calc_time:010.6f}')

