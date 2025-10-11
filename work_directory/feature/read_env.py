# 設定ファイル読み込み用です


import os
import sys
from dotenv import load_dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


load_dotenv()

user_data_dir = os.getenv("USER_DATA_DIR")
profile = os.getenv("PROFILE")
access_url=os.getenv("ACCESS_URL")


search_point_present_box=os.getenv("SEARCH_POINT_PRESENT_BOX")
search_point_present_box_ok_button=os.getenv("SEARCH_POINT_PRESENT_BOX_OK_BUTTON")
search_get_point_button=os.getenv("SEARCH_GET_POINT_BUTTON")
search_mission_receive_button=os.getenv("SEARCH_MISSION_RECEIVE_BUTTON")
search_mission_receive_ok_button=os.getenv("SEARCH_MISSION_RECEIVE_OK_BUTTON")


search_edit=os.getenv("SEARCH_EDIT")
