---
offset: "0x0050ca80"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0050ca80 — `CGChat_OnRaidInstanceMessage`

- **Адрес (Offset):** `0x0050ca80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0050ca80
int32_t CGChat::OnRaidInstanceMessage(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0050ca80 в IDA Pro / Ghidra
