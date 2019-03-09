# pylint: disable=c0111
from nbhosting.courses import (
    Track, Section, Notebook,
    notebooks_by_pattern, track_by_directory,
    DEFAULT_TRACK)

def tracks(coursedir):
    """
    coursedir is a CourseDir object that points
    at the root directory of the filesystem tree
    that holds notebooks
    track is a name that is set by the nbhosting admin,
    by default it is "course" which would mean the full
    course, but you can define alternate tracks among the
    course material

    result should be a dictionary of
    trackname -> Track instance
    """

    french_week_names = {
        'w1': "ADN et séquences génomiques",
        'w2': "gènes et protéines",
        'w3': "prédiction des gènes",
        'w4': "comparaison de séquences",
        'w5': "arbres phylogénétiques",
    }

    english_week_names = {
        'w1': "genomic texts",
        'w2': "genes & proteins",
        'w3': "gene prediction",
        'w4': "sequence comparison",
        'w5': "phylogenetic trees",
    }

    # the naming scheme is based on the language
    def _track(lang_prefix, week_names):
        return track_by_directory(
            coursedir,
            notebooks_by_pattern(coursedir, f"w?/{lang_prefix}-w?-s*.ipynb"),
            dir_labels = week_names)

    return {
        DEFAULT_TRACK: _track("fr", french_week_names),
        'english': _track("en", english_week_names),
    }
