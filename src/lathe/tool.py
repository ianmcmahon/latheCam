__author__ = 'imcmahon'


class Tool (object):
    """ represents a tool, which includes its turret station, nose radius, orientation, clearance angles, and feed/speed info """
    def __init__(self, station):
        self.station = station

        # dummy values for testing
        self.sfm = 100 # sfm, for cutting 1018
        self.chipload = 0.005
        self.min_doc = 0.010
        self.max_doc = 0.050

