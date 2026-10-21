---
offset: "0x008c32c0"
module: "Engine/Source"
file: "Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x008c32c0 — `HidDevice_WriteCompletion`

- **Адрес (Offset):** `0x008c32c0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SteelseriesMouse/Win64/HidManagerImpl.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x008c32c0
VOID CALLBACK HidDevice::WriteCompletion(DWORD error, DWORD bytes, LPOVERLAPPED overlapped) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x008c32c0 в IDA Pro / Ghidra
