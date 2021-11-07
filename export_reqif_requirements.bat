( xcopy .\docs\reqif\ .\output\reqif\ /Y)
( xcopy .\tests\unit\strictdoc\import\reqif\ .\output\reqif\ /Y)
( xcopy .\tests\integration\reqif\01-full-import\ .\output\reqif_full_integration\ /Y)
( cmd /k poetry run strictdoc export .\output\reqif --experimental-enable-file-traceability --output-dir output\ )

:: change following with other Poetry Command to use the full integration Test!
:: ( cmd /k poetry run strictdoc export .\output\reqif_full_integration --experimental-enable-file-traceability --output-dir output\reqif_full_integration )

