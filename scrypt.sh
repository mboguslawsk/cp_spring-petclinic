#!/bin/bash
sed -i '' '$d' pom.xml

cat <<EOF >> pom.xml
  <distributionManagement>
    <repository>
      <id>artifact-registry</id>
      <url></url>
    </repository>
  </distributionManagement>
</project>
EOF
