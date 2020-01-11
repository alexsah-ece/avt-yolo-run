import os
from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "dir",
        type=str,
        help="Directory to batch run yolo img evaluation"
    )
    return parser.parse_args()

if "__name__ == __main__":
    
    args = get_args()

    files = os.listdir(args.dir)
    images = [file for file in files if "jpg" in file]
    txts = [file for file in files if "txt" in file]
    total = len(images)
    print(total)
    processed = 0
    for image in images:
        print(image)
        txt = image.split(".")[0] + '.txt'
        if(txt not in txts):
            cmd = f"python yolo.py --image \"{args.dir}{os.sep}{image}\" --yolo yolo-coco --confidence 0.5"
            os.system(cmd)
        processed += 1
        print(f"Processed {processed}/{total}")