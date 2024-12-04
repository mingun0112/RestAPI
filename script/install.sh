#!/bin/bash

sudo apt update && sudo apt upgrade
sudo apt install python3-pip
sudo apt install python3.10-venv 
sudo apt install uvicorn
# 메인 스크립트
echo "NVM 및 Node.js 설치를 시작합니다..."

# NVM 설치 스크립트 실행
bash install_nvm.sh
if [ $? -ne 0 ]; then
    echo "NVM 설치에 실패하여 스크립트를 종료합니다."
    exit 1
fi

# Node.js 설치 스크립트 실행
bash install_node.sh
if [ $? -ne 0 ]; then
    echo "Node.js 설치에 실패하여 스크립트를 종료합니다."
    exit 1
fi

echo "모든 작업이 완료되었습니다!"


