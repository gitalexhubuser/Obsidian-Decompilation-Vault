---
offset: "0x008c3a80"
module: "Engine/Source"
file: "Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008c3a80 — `HidDevice_HidDevice`

- **Адрес (Offset):** `0x008c3a80`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c3a80
HidDevice::HidDevice() : m_thread(nullptr), m_threadId(0), m_threadProc(nullptr), m_file(nullptr), m_preparsedData(nullptr), m_readBufferSize(0), m_readEvent(nullptr), m_writeEvent(nullptr), m_readPending(0), m_manager(nullptr), m_readSignal(nullptr), m_stopEvent(nullptr), m_stale(0), m_devInst(0) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c3a80 в IDA Pro / Ghidra
