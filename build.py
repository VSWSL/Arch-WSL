import os
import sys
import shutil

PROGRAM_FILES = os.environ["ProgramFiles"]
VISUAL_STUDIO_INSTALLED_VERSION = 2022
VISUAL_STUDIO_INSTALLED_VARIANT = ["Community", "Professional", "Enterprise"]

MS_BUILD_PATH = (
    "{}\\Microsoft Visual Studio\\{}\\{}\\MSBuild\\Current\\Bin\\MSBuild.exe"
)

for variant in VISUAL_STUDIO_INSTALLED_VARIANT:
    if os.path.exists(
        MS_BUILD_PATH.format(PROGRAM_FILES, VISUAL_STUDIO_INSTALLED_VERSION, variant)
    ):
        MS_BUILD_PATH = MS_BUILD_PATH.format(
            PROGRAM_FILES, VISUAL_STUDIO_INSTALLED_VERSION, variant
        )
        break

PROJECT_SOLUTION_PATH = os.path.join(os.path.curdir, "ArchWSL.sln")
MS_BUILD_TARGET = "Build"
MS_BUILD_CONFIG = "Debug"

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].startswith("--target="):
            MS_BUILD_TARGET = sys.argv[i].split("=")[1].capitalize()
            if MS_BUILD_TARGET == "Clean":
                break
        elif sys.argv[i].startswith("--config="):
            MS_BUILD_CONFIG = sys.argv[i].split("=")[1].capitalize()

BUILD_COMMAND = '"{}" {} /t:{} /m /nr:true /p:Configuration={}'

BUILD_COMMAND = BUILD_COMMAND.format(
    MS_BUILD_PATH,
    PROJECT_SOLUTION_PATH,
    MS_BUILD_TARGET,
    MS_BUILD_CONFIG,
)

exitCode = os.system(BUILD_COMMAND)

if MS_BUILD_TARGET == "Clean":
    cleanDirs = [
        "ArchWSL\\x64",
        "ArchWSL\\ARM64",
        "ArchWSL-Appx\\x64",
        "ArchWSL-Appx\\ARM64",
        "ArchWSL-Appx\\BundleArtifacts",
        "x64\\Debug",
        "x64\\Release",
        "AppPackages",
    ]

    cleanFiles = [
        "ArchWSL-Appx\\ArchWSL-Appx.vcxproj.user",
        "ArchWSL\\ArchWSL.vcxproj.user",
        "ArchWSL\\MSG00409.bin",
    ]

    for cleanDir in cleanDirs:
        if os.path.exists(cleanDir):
            shutil.rmtree(cleanDir)

    for cleanFile in cleanFiles:
        if os.path.exists(cleanFile):
            os.remove(cleanFile)

sys.exit(exitCode)
