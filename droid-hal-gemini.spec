# These and other macros are documented in dhd/droid-hal-device.inc
%define device gemini
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 5
%define installable_zip 1
%define droid_target_aarch64 1

# define device_target_cpu aarch64
%define straggler_files \
        /init.qcom.sh \
        /bugreports \
        /d \
        /file_contexts.bin \
        /property_contexts \
        /sdcard \
        /selinux_version \
        /service_contexts \
        /vendor \
        %{nil}

%include rpm/dhd/droid-hal-device.inc
