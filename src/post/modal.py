__author__ = 'imcmahon'

class Stackable (object):
    def __init__(self):
        self.w = None

    def get_stack(self, stack_name):
        stack_name = "__stack__%s" % (stack_name, )
        if not hasattr(self, stack_name):
            setattr(self, stack_name, [])
        return getattr(self, stack_name)

    def pop(self, stack_name):
        stack_name = "__stack__%s" % (stack_name, )
        stack = getattr(self, stack_name)
        stack.pop()
        try:
            last_block = stack[-1]
            self.w(last_block)
        except IndexError:
            pass

class Modal_Feed (Stackable):
    """ contains all the feed related modal methods """

    def __init__(self):
        super(Modal_Feed, self).__init__()
        self.w = None

    def push_modal_feed_inverse_time(self):
        self.get_stack("feed").append("G93")
        self.w("G93")

    def push_modal_feed_upm(self):
        self.get_stack("feed").append("G94")
        self.w("G94")

    def push_modal_feed_ipm(self):
        self.push_modal_feed_upm()

    def push_modal_feed_mmpm(self):
        self.push_modal_feed_upm()

    def push_modal_feed_upr(self):
        self.get_stack("feed").append("G95")
        self.w("G95")

    def push_modal_feed_ipr(self):
        self.push_modal_feed_upr()

    def push_modal_feed_mmpr(self):
        self.push_modal_feed_upr()

    def pop_modal_feed(self):
        self.pop("feed")

class Modal_Spindle_Speed (Stackable):
    """ contains all the spindle speed related modals """

    def __init__(self):
        super(Modal_Spindle_Speed, self).__init__()
        self.w = None

    def push_modal_rpm(self):
        self.get_stack("sspeed").append("G97")
        self.w("G97")

    def push_modal_css(self, speed, maxrpm = None):
        block = "G96 S%s %s" % (speed, ("D%s"%(maxrpm,)) if maxrpm is not None else "")
        self.get_stack("sspeed").append(block)
        self.w(block)

    def pop_modal_speed(self):
        self.pop("sspeed")




class Modal (Modal_Feed, Modal_Spindle_Speed):
    """ contains all the modal methods  """
