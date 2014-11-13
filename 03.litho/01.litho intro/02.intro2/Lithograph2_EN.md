Resolution in projection systems[edit]

Main articles: Optics#Diffraction and optical resolution, Diffraction, and Optical resolution


The filtered fluorescent lighting in photolithography cleanrooms contains no ultraviolet or blue light in order to avoid exposing photoresists. The spectrum of light emitted by such fixtures gives virtually all such spaces a bright yellow color.

The ability to project a clear image of a small feature onto the wafer is limited by the wavelength of the light that is used, and the ability of the reduction lens system to capture enough diffraction orders from the illuminated mask. Current state-of-the-art photolithography tools use deep ultraviolet (DUV) light from excimer lasers with wavelengths of 248 and 193 nm (the dominant lithography technology today is thus also called "excimer laser lithography"), which allow minimum feature sizes down to 50 nm. Excimer laser lithography has thus played a critical role in the continued advance of the so-called Moore’s Law for the last 20 years (see below[3]).
The minimum feature size that a projection system can print is given approximately by:
CD = k_1 \cdot\frac{\lambda}{NA}
where
\,CD is the minimum feature size (also called the critical dimension, target design rule). It is also common to write 2 times the half-pitch.
\,k_1 (commonly called k1 factor) is a coefficient that encapsulates process-related factors, and typically equals 0.4 for production. The minimum feature size can be reduced by decreasing this coefficient through Computational lithography.
\,\lambda is the wavelength of light used
\,NA is the numerical aperture of the lens as seen from the wafer
According to this equation, minimum feature sizes can be decreased by decreasing the wavelength, and increasing the numerical aperture (to achieve a tighter focused beam and a smaller spot size). However, this design method runs into a competing constraint. In modern systems, the depth of focus is also a concern:
D_F = k_2 \cdot\frac{\lambda}{{NA}^2}
Here, \,k_2 is another process-related coefficient. The depth of focus restricts the thickness of the photoresist and the depth of the topography on the wafer. Chemical mechanical polishing is often used to flatten topography before high-resolution lithographic steps.