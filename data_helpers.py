import subprocess as s
from pathlib import Path

# call the file to run them in order or use the methods individually (in order still)

def run_n4_iteratively():
    s.run(["mkdir", "/home/sabino/task_driven_data_augmentation/dataset/summer_bias_correct/1label"])
    # s.run(["mkdir", "/home/sabino/task_driven_data_augmentation/dataset/cardiac_bias_correct"])
    for index in range(1, 16):
        # Load each image
        if index < 10:
            test_id = "00" + str(index)
        elif index < 100:
            test_id = "0" + str(index)
        else:
            test_id = str(index)

        inputPath = (
            "/home/sabino/task_driven_data_augmentation/dataset/summer_data_home/images/patient"
            # "/home/sabino/task_driven_data_augmentation/dataset/training/patient"
            + test_id
            + "/patient"
            + test_id
            # + "_frame01.nii.gz"
            + ".nii.gz"
        )
        outputPath = (
            "/home/sabino/task_driven_data_augmentation/dataset/summer_bias_correct/1label/patient"
            + test_id
        )

        # create output directory
        s.run(
            [
                "mkdir",
                outputPath,
            ]
        )

        # run N4_th on each patient frame01 image
        s.run(
            [
                "./N4_th",
                inputPath,
                outputPath + "/patient" + test_id + ".nii.gz", #"_frame01.nii.gz",
                # outputPath + "/patient" + test_id + "_frame01.nii.gz", 
                "0.001",
            ]
        )

    # run n4_th once more for patient090 who has no "patient090_frame01.nii.gz" image
    # s.run(
    #    [
    #        "./N4_th",
    #        "/home/sabino/task_driven_data_augmentation/dataset/training/patient090/patient090_frame04.nii.gz",
    #        "/home/sabino/task_driven_data_augmentation/dataset/cardiac_bias_correct/patient090/patient090_frame04.nii.gz",
    #        "0.001",
    #    ]
    # )


def add_labels_to_dataset():
    # copy labels from dataset/training/patient001_frame01_gt.nii.gz to
    # dataset/bias_correct/patient001_frame01_gt.nii.gz to

    # inputPath = "/home/sabino/task_driven_data_augmentation/dataset/training/patient"
    # inputPath = "/home/sabino/nvidia-dg-research/all_models/summer_model/data/labelsTr/patient"
    inputPath = "/home/sabino/task_driven_data_augmentation/dataset/summer_data_home/4label/patient"
    outputBasePath = (
        "/home/sabino/task_driven_data_augmentation/dataset/summer_bias_correct/4label/patient"
    )

    for index in range(1, 16):
        if index < 10:
            test_id = "00" + str(index)
        elif index < 100:
            test_id = "0" + str(index)
        else:
            test_id = str(index)

        inputAbsolutePath = (
            inputPath + test_id + ".nii.gz"
            # inputPath + test_id + "/patient" + test_id + "_frame01_gt.nii.gz"
        )
        outputAbsolutePath = (
            outputBasePath + test_id + "/patient" + test_id + "_gt.nii.gz"
            # outputBasePath + test_id + "/patient" + test_id + "_frame01_gt.nii.gz"
        )

        s.run(["cp", inputAbsolutePath, outputAbsolutePath])

        # pathlist = Path(inputPath).rglob("*_frame01.nii.gz")
        # for path in pathlist:
        #     print(str(pathlist))

    # once more for patient090 special case
    # s.run(
    #    [
    #        "cp",
    #        inputPath + "090/patient090_frame04_gt.nii.gz",
    #        outputBasePath + "090/patient090_frame04_gt.nii.gz",
    #    ]
    # )

# run_n4_iteratively()
# add_labels_to_dataset()