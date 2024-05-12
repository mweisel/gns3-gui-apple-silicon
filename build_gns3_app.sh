# Delete existing build and dist directories
for dir in build dist; do
  if [ -d ${dir} ]; then
    rm -rf ${dir}
  fi
done

# Create the GNS3.app bundle
pyinstaller gns3.spec

# Add the schemas directory to the GNS3.app bundle
if [ -d 'dist/GNS3.app' ]; then
  cp -R src/gns3/schemas dist/GNS3.app/Contents/MacOS
fi
