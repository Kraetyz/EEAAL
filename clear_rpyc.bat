@ECHO OFF
cd ".\EEAAL\game\scripts"
call :treeProcess
goto :eof

:treeProcess
rem Do whatever you want here over the files of this subdir, for example:
for %%f in (*.rpyc) do del %%f
for /D %%d in (*) do (
    echo %%d
    cd %%d
    call :treeProcess
    cd ..
)
