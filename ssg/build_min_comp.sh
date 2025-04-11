zola build

src="public"
dst="dest"

cp -R "$src"/. "$dst" && cd "$dst"


minhtml $(find . -type f -a -name "*\.html" -o -name "*\.xml" ) 
css_files=$(find . -type f -name "*\.css" )
echo "$css_files" | while read -r file
do
	lightningcss --minify  "$file" -o  "$file"
done

files=$(find . -type f -a -name "*\.html" -o -name "*\.css" -o -name "*\.js" -o -name "*\.xml" )
echo "$files" | while read -r file
do
	gzip -9 < "$file" > "$file.gz"
done

