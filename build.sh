#!/bin/bash
find . -name "*.pyc" -exec rm '{}' ';'
rm dist/GTDtoCSV.zip
rm dist/GTDtoCSV.tar.gz
mv src GTDtoCSV
tar -pczf dist/GTDtoCSV.tar.gz   --exclude=".*" --exclude="/.*" --exclude="/*/.*" --exclude="*.pyc" ./GTDtoCSV
mv GTDtoCSV/GTDtoCSV GTDtoCSV/GTDtoCSV.py
zip -r dist/GTDtoCSV.zip GTDtoCSV/[!\.]* -x \*/\.*
mv GTDtoCSV/GTDtoCSV.py GTDtoCSV/GTDtoCSV
mv GTDtoCSV src