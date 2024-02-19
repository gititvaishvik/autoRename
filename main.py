import os
import gc
import time
import cv2


def rename_with_incremental(filename):
    base_name, extension = os.path.splitext(filename)
    new_filename = filename
    counter = 1

    while os.path.exists(new_filename):
        new_filename = f"{base_name}_{counter}{extension}"

        counter += 1

    return new_filename


def always_find(directory, min_, file_names):
    waitcounter = min_ * 60
    full_paths = [os.path.join(directory, file_name) for file_name in file_names]

    if all(os.path.exists(full_path) for full_path in full_paths):
        modified_times = [os.path.getmtime(full_path) for full_path in full_paths]
        while waitcounter:
            #         print(full_path)
            if any(modified_time != os.path.getmtime(full_path) for modified_time, full_path in
                   zip(modified_times, full_paths)):
                time.sleep(1)
                for full_path in full_paths:
                    write_img(directory, full_path)
                modified_times = [os.path.getmtime(full_path) for full_path in full_paths]

                waitcounter = min_ * 60
            else:
                time.sleep(1)
                waitcounter -= 1


def write_img(directory, full_path):
    new_filename = rename_with_incremental(full_path)
    new_full_path = os.path.join(directory, new_filename)
    print(new_full_path)
    iris_img = cv2.imread(full_path)

    cv2.imwrite(new_full_path, iris_img)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = r"C:\Users\Mantra\Documents\apps\Iris_App\Marvis_Enroll\x64"
    stop_flag = False
    files_to_check = ("LeftIris.bmp", "RightIris.bmp")
    always_find(path, 5, files_to_check)
