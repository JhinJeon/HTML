# 개인 프로젝트 개요

## 0.파일 설명

- Tutorial : HTML의 가장 기본적인 기능을 익히기 위해 만든 HTML 파일들입니다.
- personal_project : 진행 중인 개인 프로직트입니다.

## 기획 내용

- 웹 기반의 금칙어 끝말잇기 게임 페이지 제작 프로젝트입니다.
- 끝말잇기 룰에서 특정 낱말을 입력했을 때 패배하는 룰이 추가되었습니다.
- 금칙은 플레이어의 단어 입력 패턴을 학습하여, 자주 사용하는 낱말을 금칙으로 제시합니다.

## 기획 의도

- 웹 기반의 미니게임은 많지만, 시스템에 익숙한 사람과 그렇지 않은 사람과의 간극, 소위 '뉴비'와 '고인물'의 편차가 심한 경우가 많습니다.
- 끝말잇기라는 친숙한 소재를 사용하여 게임 룰에 대해 잘 몰라도 쉽게 입문할 수 있도록 하고, 뉴비와 고인물이 함께 어우러져서 재미있게 즐길 수 있는 콘텐츠입니다.
- 아이스 브레이킹 등의 환경에서 게임 이해도에 따른 편차를 최소화하면서, 게임 룰을 빠르게 익혀서 다른 사람들과 함께 가볍고 재미있게 즐길 수 있는 콘텐츠입니다.

## 게임 규칙

- 매 라운드마다 각 플레이어는 금지 낱말을 배정받습니다. 
- 각 플레이어는 다른 플레이어의 금칙어를 알 수 있습니다. 단, 자신의 금칙어는 알 수 없습니다.
- 금칙어를 입력한 플레이어는 즉시 탈락하고, 생존자들끼리 게임을 진행합니다. 탈락자는 게임을 관전하거나 퇴장할 수 있습니다.
- 탈락한 플레이어가 발생하거나, 모든 플레이어들이 탈락자 없이 단어를 일정 수 이상 입력한 경우 다음 라운드로 진행합니다.
- 다음 라운드로 진행되는 경우 기존의 금칙어에 새로운 금칙어가 추가됩니다. 이 때 플레이어는 자신의 것을 제외한 다른 플레이어들의 금칙어를 알 수 있습니다.
- 최후의 생존자 1인이 남으면 승리합니다.

## 진행 과정

1. 게임 상황 별 웹 페이지 만들기
   1. 메인 페이지(미완성)
   2. 게임 진행 페이지(미완성)
   3. 탈락 화면 페이지(미완성)
   4. 승리 페이지(미완성)
   5. 관전 페이지(미완성)

2. 서버 환경 구축
3. 네이버 사전 API와 연동