import os
import re
import time
from abc import ABCMeta, abstractmethod
from cgitb import reset

from aoc2022.common.io import load_file
from os.path import splitext, exists
import logging

logger = logging.getLogger("AOC Base")


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

    def part_1(self, filename: str) -> int:
        data = load_file(filename, self.load_handler_part1)
        result = self.calc_1(data)

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

        return filename, expected == result, expected, result

    def part_2(self, filename: str) -> int:
        data = load_file(filename, self.load_handler_part2)
        result = self.calc_2(data)

        split_filename = splitext(filename)
        expected_filename = split_filename[0] + "_result" + split_filename[1]
        if not exists(expected_filename):
            with open(expected_filename, 'w') as f:
                print(-1, file=f)
        expected = type(result)(load_file(expected_filename)[0])
        return filename, expected == result, expected, result

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
                results += [result + (took,)]
        return results

    def run_part_2(self, filepath: str) -> []:
        results = []
        if filepath is not None and len(filepath) > 0:
            filenames = self.glob_re(filepath, os.listdir())
            for filename in filenames:
                start = time.perf_counter()
                result = self.part_2(filename)
                took = time.perf_counter() - start
                results += [result + (took,)]
        return results

    def run(self, part1_path: str, part2_path: str) -> []:
        results = { "Part 1":self.run_part_1(part1_path), "Part 2": self.run_part_2(part2_path)}
        print(f'{"":21s} {"Expected":30s} {"Actual":30s} {"Time (s.ms)":8s}')
        self.display(results, "Part 1")
        self.display(results, "Part 2")
        failed = False
        for result in results:
            for runs in results:
                if not runs[1]:
                    failed = True
                    break;
        return failed, results

    def display(self, results, part):
        print(f'{part:21s}')
        for result in results[part]:
            star = '*'
            if result[1]:
                star = ' '
            print(f'{star}{result[0]:20s} {str(result[2]):30s} {str(result[3]):30s} {result[4]:010.6f}')
