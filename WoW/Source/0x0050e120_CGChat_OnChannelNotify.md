---
offset: "0x0050e120"
module: "WoW/Source"
file: "WoW/Source/Ui/ChatFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0050e120 — `CGChat_OnChannelNotify`

- **Адрес (Offset):** `0x0050e120`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Ui/ChatFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0050e120
int32_t CGChat::OnChannelNotify(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0050e120 в IDA Pro / Ghidra
