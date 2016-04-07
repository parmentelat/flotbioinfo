# -*- coding: utf-8 -*-

from __future__ import print_function

import re

from .exercice_function import ExerciceFunction

class ExerciceRegexp(ExerciceFunction):
    """
    With these exercices the students are asked to write a regexp
    which is transformed into a function that essentially
    takes an input string and returns a boolean
    that says if the *whole* string matches or not
    """
    @staticmethod
    def regexp_to_solution(regexp, match_otherwise_search):
        def solution(string):
            match = re.match(regexp, string) if match_otherwise_search \
                    else re.search(regexp, string)
            if not match:
                return False
            else:
                # exo with match_otherwise_search display yes or no
                if match_otherwise_search:
                    return match.group(0) == string
                # the other ones will show the beginning and end of match
                else:
                    return match.span()
        return solution

    def __init__(self, name, regexp, inputs, match_otherwise_search=True, *args, **keywords):
        """
        a regexp exercice is made with
        . a user-friendly name
        . a regexp string for the solution
        . a list of inputs on which to run the regexp
        . match_otherwise_search is a boolean that says if we want to run `match` or `search`
        . additional settings from ExerciceFunction
        """
        solution = ExerciceRegexp.regexp_to_solution(regexp, match_otherwise_search)
        ExerciceFunction.__init__(self, solution, inputs, *args, **keywords)
        self.regexp = regexp
        self.name = name
        self.match_otherwise_search = match_otherwise_search
        self.render_name = False

    def correction(self, student_regexp):
        student_solution = ExerciceRegexp.regexp_to_solution(student_regexp, self.match_otherwise_search)
        return ExerciceFunction.correction(self, student_solution)

##############################
class ExerciceRegexpGroups(ExerciceFunction):
    """
    With these exercices the students are asked to write a regexp
    with a set of specified named groups
    a list of these groups needs to be passed to construct the object

    the regexp is then transformed into a function that again
    takes an input string and either a list of tuples 
    (groupname, found_substring) 
    or None if no match occurs
    """

    @staticmethod
    def extract_group(match, group):
        try:        return group, match.group(group)
        except:     return group, "Undefined"

    @staticmethod
    # match_otherwise_search mode not implemented yet
    def regexp_to_solution(regexp, groups):
        def solution(string):
            match = re.match(regexp, string)
            return match and [ExerciceRegexpGroups.extract_group(match, group)
                              for group in groups]
        return solution

    def __init__(self, name, regexp, groups, inputs, *args, **keywords):
        solution = ExerciceRegexpGroups.regexp_to_solution(regexp, groups)
        ExerciceFunction.__init__(self, solution, inputs, *args, **keywords)
        self.name = name
        self.regexp = regexp
        self.groups = groups
        self.render_name = False

    def correction(self, student_regexp):
        student_solution = ExerciceRegexpGroups.regexp_to_solution(student_regexp, self.groups)
        return ExerciceFunction.correction(self, student_solution)
