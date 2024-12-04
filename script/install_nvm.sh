#!/bin/bash

# NVM 설치
echo "NVM 설치 스크립트를 실행합니다..."

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# 현재 셸에서 NVM을 사용할 수 있도록 설정
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # nvm 명령어 로드

# 설치 확인
if command -v nvm &> /dev/null; then
    echo "NVM 설치가 완료되었습니다."
else
    echo "NVM 설치에 실패했습니다."
    exit 1
fi
