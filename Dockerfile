FROM archlinux:latest

# work
RUN echo "Server = http://mirror.rackspace.com/archlinux/\$repo/os/\$arch" > /etc/pacman.d/mirrorlist

RUN pacman -Sy --noconfirm \
    && pacman -S --noconfirm sudo

RUN useradd -m -s /bin/bash stasnocap \
    && echo "stasnocap:1" | chpasswd \
    && usermod -aG wheel stasnocap \
    && echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER stasnocap
WORKDIR /home/stasnocap
COPY --chown=stasnocap:stasnocap ./work/ .

WORKDIR /home/stasnocap/dev
COPY --chown=stasnocap:stasnocap . .

ENV DEV_ENV=/home/stasnocap/dev
RUN ./dev-env
