---
offset: "0x0050cda0"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0050cda0 — `CGChat_OnInstanceResetFailed`

- **Адрес (Offset):** `0x0050cda0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0050cda0
int32_t CGChat::OnInstanceResetFailed(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0050cda0 в IDA Pro / Ghidra
