---
offset: "0x008c3a10"
module: "Engine/Source"
file: "Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008c3a10 — `HidDevice_HidDevice`

- **Адрес (Offset):** `0x008c3a10`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c3a10
HidDevice::HidDevice(DWORD devInst) : m_thread(nullptr), m_threadId(0), m_threadProc(nullptr), m_file(nullptr), m_preparsedData(nullptr), m_readSignal(nullptr), m_stopEvent(nullptr), m_devInst(devInst) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c3a10 в IDA Pro / Ghidra
