import os
import sys
import shutil

PROGRAM_FILES_DIRS = [
    d for d in (
        os.environ.get("ProgramFiles"),
        os.environ.get("ProgramFiles(x86)"),
    ) if d
]
VISUAL_STUDIO_INSTALLED_VERSION = 2022
VISUAL_STUDIO_INSTALLED_VARIANT = ["Community", "Professional", "Enterprise", "BuildTools"]

MS_BUILD_PATH_TEMPLATE = '{}\\Microsoft Visual Studio\\{}\\{}\\MSBuild\\Current\\Bin\\MSBuild.exe'
MS_BUILD_PATH = None

for program_files in PROGRAM_FILES_DIRS:
    for variant in VISUAL_STUDIO_INSTALLED_VARIANT:
        candidate = MS_BUILD_PATH_TEMPLATE.format(
            program_files, VISUAL_STUDIO_INSTALLED_VERSION, variant
        )
        if os.path.exists(candidate):
            MS_BUILD_PATH = candidate
            break
    if MS_BUILD_PATH:
        break

if not MS_BUILD_PATH:
    # Fall back to MSBuild on PATH (e.g. added by microsoft/setup-msbuild).
    MS_BUILD_PATH = shutil.which("MSBuild") or shutil.which("MSBuild.exe") or "MSBuild.exe"

PROJECT_SOLUTION_PATH = os.path.join(os.path.curdir, 'ArchWSL.sln')
MS_BUILD_TARGET = "Build"
MS_BUILD_CONFIG = "Debug"
MS_BUILD_PLATFORM = "x64"

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        if sys.argv[i].startswith("--target="):
            MS_BUILD_TARGET = sys.argv[i].split("=")[1].capitalize()
            if MS_BUILD_TARGET == "Clean":
                break
        elif sys.argv[i].startswith("--config="):
            MS_BUILD_CONFIG = sys.argv[i].split("=")[1].capitalize()
        elif sys.argv[i].startswith("--platform="):
            MS_BUILD_PLATFORM = sys.argv[i].split("=")[1]

BUILD_COMMAND = "\"{}\" {} /t:{} /m /nr:true /p:Configuration={};Platform={}"

BUILD_COMMAND = BUILD_COMMAND.format(
    MS_BUILD_PATH,
    PROJECT_SOLUTION_PATH,
    MS_BUILD_TARGET,
    MS_BUILD_CONFIG,
    MS_BUILD_PLATFORM
)

exitCode = os.system(BUILD_COMMAND)

if (MS_BUILD_TARGET == "Clean"):
    cleanDirs = [
        "ArchWSL\\x64",
        "ArchWSL\\ARM64",
        "ArchWSL-Appx\\x64",
        "ArchWSL-Appx\\ARM64",
        "ArchWSL-Appx\\BundleArtifacts",
        "x64\\Debug",
        "x64\\Release",
        "AppPackages"
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
