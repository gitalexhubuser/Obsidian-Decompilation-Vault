---
offset: "0x004695f0"
module: "WoW/Source"
file: "WoW/Source/WowServices/WowConnectionNet.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004695f0 — `WowConnectionNet_WowConnectionNet`

- **Адрес (Offset):** `0x004695f0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WowConnectionNet.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004695f0
WowConnectionNet::WowConnectionNet(int32_t numThreads, void (*threadInit)()) : m_stopEvent(1, 0), m_workerSemaphore(0, numThreads), m_serviceSemaphore(0, 0x7FFFFFFF) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004695f0 в IDA Pro / Ghidra
