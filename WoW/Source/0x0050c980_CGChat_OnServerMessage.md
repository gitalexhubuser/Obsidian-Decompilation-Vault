---
offset: "0x0050c980"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0050c980 — `CGChat_OnServerMessage`

- **Адрес (Offset):** `0x0050c980`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0050c980
int32_t CGChat::OnServerMessage(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0050c980 в IDA Pro / Ghidra
