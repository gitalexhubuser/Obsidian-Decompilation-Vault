---
offset: "0x00500240"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00500240 — `CGChat_OnVoiceStatusChanged`

- **Адрес (Offset):** `0x00500240`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00500240
int32_t CGChat::OnVoiceStatusChanged(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00500240 в IDA Pro / Ghidra
