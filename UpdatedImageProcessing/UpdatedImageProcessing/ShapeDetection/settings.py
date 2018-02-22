

class ShapeDetectionSettings(object):

    # shape_classification.py
    CIRCLE_SCORE_THRESHOLD = 0.45
    NOISE_SCORE_THRESHOLD = 0.6
    SQUARE_RECTANGLE_EIGEN_RATIO_THRESHOLD = 1.5
    PENTAGON_STAR_CLUSTER_THRESHOLD = 8
    OCTAGON_CROSS_CLUSTER_THRESHOLD = 10

    SHAPE_CHOICES = ("circle", "semicircle", "quarter_circle", "triangle", "square", "rectangle", "trapezoid", "pentagon", "hexagon", "heptagon", "octagon", "star", "cross")

    # polar_side_counter.py
    CIRCLE_DERIV_RANGE = (0.96, 1.04)
    NOISE_DERIV_RANGE = (0.80, 1.20)
