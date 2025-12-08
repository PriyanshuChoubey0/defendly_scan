if exist "%USERPROFILE%\Defendly\.Defendly_JVM.properties" (
	set /p jvmopts=< "%USERPROFILE%\Defendly\.Defendly_JVM.properties"
) else (
	set jvmopts=-Xmx512m
)

java %jvmopts% -jar zap-D-2025-12-05.jar %*
