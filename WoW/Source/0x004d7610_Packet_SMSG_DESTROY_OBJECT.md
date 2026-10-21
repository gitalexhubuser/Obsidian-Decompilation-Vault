---
offset: "0x004d7610"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d7610 — `Packet_SMSG_DESTROY_OBJECT`

- **Адрес (Offset):** `0x004d7610`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d7610
int32_t Packet_SMSG_DESTROY_OBJECT(void* param, NETMESSAGE msgId, uint32_t time, CDataStore* msg) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d7610 в IDA Pro / Ghidra
