#/bin/bash

find . -name '*.md' > docs.dat

while read file; do 
	file_docx=$( echo "$file".docx | sed -e 's/\.md//g')
	pandoc -o $file_docx -f markdown -t docx $file
done < docs.dat

rm docs.dat