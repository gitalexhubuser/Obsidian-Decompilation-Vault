---
offset: "0x008c3270"
module: "Engine/Source"
file: "Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008c3270 — `HidDevice_ReadCompletion`

- **Адрес (Offset):** `0x008c3270`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c3270
VOID CALLBACK HidDevice::ReadCompletion(DWORD error, DWORD bytes, LPOVERLAPPED overlapped) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c3270 в IDA Pro / Ghidra
