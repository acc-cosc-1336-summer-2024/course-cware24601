from numbers import Rational


def  get_options_ratio (options, total):
     ratio = options / total
     
     return ratio



def get_faculty_rating(ratio):
     if (ratio <= 1 and ratio >= .9):
          return 'Excellent'
     if (ratio, .9 and ratio >= .8):
          return 'Very Good'
     if (ratio, .8 and ratio >= .7):
          return 'Good'
     if (ratio, .7 and ratio, ):
          return 'Needs Improvement'
     if (ratio, .6 and ratio >= .59):
          return 'Unacceptable'