---
offset: "0x00633650"
module: "WoW/Source"
file: "WoW/Source/Net/NetClient/NetClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00633650 — `NETEVENTQUEUE_AddEvent`

- **Адрес (Offset):** `0x00633650`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Net/NetClient/NetClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00633650
void NETEVENTQUEUE::AddEvent(EVENTID eventId, void* connection, NetClient* client, const void* data, uint32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00633650 в IDA Pro / Ghidra
