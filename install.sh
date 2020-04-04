#!/bin/bash

echo "Устанавливаем зависимости"
pip3 install -r \ requirements.txt
echo "----------------------------------------------"

echo "Перемещаем в папку с программами"
cat mop.py > /bin/mop
chmod +x /bin/mop
echo "Готово!"