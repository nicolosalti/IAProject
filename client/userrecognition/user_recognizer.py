import copy
import time
import globals as glob
from threading import Thread

class UserRecognizer(Thread):
    def __init__(self, frequency=1):
        super(UserRecognizer, self).__init__()
        self._user_faces_dir = "../data/user_faces_db"
        self._frequency = frequency

    def detect_user(self, img):  # Returns the name of the user if it is registered, None otherwise
        '''
        lst = os.listdir(self._user_faces_dir)
        if len(lst) > 0:  # If there is at least one user registered
            recognition = DeepFace.find(img, db_path=self._user_faces_dir, enforce_detection=False)
            if recognition[0].empty:  # User not recognized
                return None
            else:  # User recognized
                file_name = os.path.basename(recognition[0]["identity"][0])
                name, extension = os.path.splitext(file_name)
                user_name = name.split("/")[-1]
                return user_name
        else:
            return None
        '''
        # TODO SEND MESSAGE
        return None

    def run(self):
        while not glob.stop_flag:
            time.sleep(1 / self._frequency)
            with glob.shared_frame_lock:
                img = copy.deepcopy(glob.actual_frame)
            user_name = self.detect_user(img)
            if user_name is not None:
                glob.logged_user = self._users_storage_ctrl.retrieve_user(user_name)
                glob.logged_user.set_mode(False)
                glob.controller.rotate_back_seat(glob.logged_user.get_position())
                return