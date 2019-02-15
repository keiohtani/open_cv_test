# based on https://qiita.com/hitomatagi/items/ce00fab38d829965db3b
# based on https://qiita.com/hitomatagi/items/2c3a2bfefe73ab5c86a4

import cv2

def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

if __name__ == '__main__':
    
    INTERVAL = 30
    DEVICE_ID = 0  
    ESC_KEY = 27
    FRAME_RATE = 30
    EDGE_WINDOW_NAME = 'edge'
    ORIGINAL_WINDOW_NAME = 'original'
    OUTPUT_FILE_NAME = 'edge.mov'

    cap = cv2.VideoCapture(DEVICE_ID)
    end_flag, c_frame = cap.read()
    height, width, channels = c_frame.shape
    # rec = cv2.VideoWriter(OUTPUT_FILE_NAME, cv_fourcc('X', 'V', 'I', 'D'), FRAME_RATE, (width, height), True)
    print('Press esc to exit.')

    while end_flag == True:
        gray_frame = cv2.cvtColor(c_frame, cv2.COLOR_BGR2GRAY)
        edge_frame = cv2.Canny(gray_frame, 50, 110)

        cv2.imshow(EDGE_WINDOW_NAME, edge_frame)
        # rec.write(edge_frame)

        key = cv2.waitKey(INTERVAL)
        if key == ESC_KEY:
            break

        end_flag, c_frame = cap.read()
    
    #exitting
    cv2.destroyAllWindows()
    cap.release()
