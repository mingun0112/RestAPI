#!/bin/bash

# Node.js 설치
echo "Node.js 설치 스크립트를 실행합니다..."

# NVM이 로드되지 않았으면 로드
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" || {
    echo "NVM이 로드되지 않았습니다. 설치 후 다시 시도하세요."
    exit 1
}

# Node.js 설치
NODE_VERSION="22"
nvm install $NODE_VERSION

# 설치 확인
node_version=$(node -v)
npm_version=$(npm -v)

if [[ $node_version == v22* && $npm_version ]]; then
    echo "Node.js($node_version)와 npm($npm_version)이 성공적으로 설치되었습니다."
else
    echo "Node.js 또는 npm 설치에 실패했습니다."
    exit 1
fi
