---
offset: "0x008c3e40"
module: "Engine/Source"
file: "Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008c3e40 — `HidDevice_HidDevice`

- **Адрес (Offset):** `0x008c3e40`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c3e40
HidDevice::HidDevice(const HidDevice& device) : m_thread(nullptr), m_threadId(0), m_threadProc(nullptr), m_interfaceDetail(std::move(const_cast<HidDevice&>(device).m_interfaceDetail)), m_file(device.m_file), m_openRead(device.m_openRead), m_openWrite(device.m_openWrite), m_openOverlapped(device.m_openOverlapped), m_openExclusive(device.m_openExclusive), m_preparsedData(device.m_preparsedData), m_attributes(device.m_attributes), m_caps(device.m_caps), m_writeOverlapped(device.m_writeOverlapped), m_readOverlapped(device.m_readOverlapped), m_readBuffer(std::move(const_cast<HidDevice&>(device).m_readBuffer)), m_readBufferSize(device.m_readBufferSize), m_readEvent(device.m_readEvent), m_writeEvent(device.m_writeEvent), m_readPending(device.m_readPending), m_hardwareId(device.m_hardwareId), m_manager(device.m_manager), m_readSignal(device.m_readSignal), m_stopEvent(device.m_stopEvent), m_stale(device.m_stale), m_devInst(device.m_devInst) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c3e40 в IDA Pro / Ghidra
