---
offset: "0x00507a80"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00507a80 — `InternalJoinChannel`

- **Адрес (Offset):** `0x00507a80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00507a80
bool InternalJoinChannel(const char* channelName, const char* password, uint32_t window, bool checkRecruitment, const char** zoneChannelName, int32_t* zoneChannelID, bool silent, int32_t a8, int32_t a9, uint32_t number) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00507a80 в IDA Pro / Ghidra
