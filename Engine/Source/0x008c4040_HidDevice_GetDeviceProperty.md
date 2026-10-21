---
offset: "0x008c4040"
module: "Engine/Source"
file: "Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008c4040 — `HidDevice_GetDeviceProperty`

- **Адрес (Offset):** `0x008c4040`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c4040
bool HidDevice::GetDeviceProperty(HDEVINFO deviceInfoSet, PSP_DEVINFO_DATA deviceInfoData, DWORD property, std::string& value) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c4040 в IDA Pro / Ghidra
