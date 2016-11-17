#source ~/cryocon/buildroot/m54/staging/usr/share/buildroot/gdbinit
#set solib-search-path ~/cryocon/buildroot/m54/build/xdriver_xf86-video-fbdev-0.4.4/src/.libs/
#set solib-search-path ~/cryocon/buildroot/output/build/lighttpd-1.4.39/src/.libs/
#add-auto-load-safe-path ~/cryocon/buildroot/m54/host/usr/arm-buildroot-linux-gnueabi/sysroot/usr/lib/libstdc++.so.6.0.20-gdb.py
#target extended-remote revb:2345
add-auto-load-safe-path /home/nicholaswalton/cryocon/.gdbinit
