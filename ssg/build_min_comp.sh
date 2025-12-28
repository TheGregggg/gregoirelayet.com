zola build

src="public"
dst="dest"

rm -Rf "$dst"

cp -R "$src"/. "$dst" && cd "$dst"

# minhtml --keep-closing-tags --keep-html-and-head-opening-tags  $(find . -type f -a -name "*\.html" -o -name "*\.xml" ) 

css_files=$(find . -type f -name "*\.css" )
echo "$css_files" | while read -r file
do
	lightningcss --minify  "$file" -o  "$file"
done

files=$(find . -type f -a -name "*\.html" -o -name "*\.css" -o -name "*\.js" -o -name "*\.xml" -o -name "*\.ttf" )
echo "$files" | while read -r file
do
	gzip -9 < "$file" > "$file.gz"
done

