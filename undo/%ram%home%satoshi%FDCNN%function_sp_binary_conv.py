Vim�UnDo� ��y>|�)7`p�50��~a��5���E*L�G�  �                  	       	   	   	    YS    _�                     [       ����                                                                                                                                                                                                                                                                                                                            [          f          v       YS*     �   e   g          ;        feature = numpy.real(feature).astype(numpy.float32)�   d   f          6        feature = ifft2(feature_f)[:,:,h-oh:h, w-ow:w]�   c   e           �   b   d          B            feature_f[i,:,:,:] = (x_f_ex[i,:,:,:,:] * Wb_f).sum(1)�   a   c          C            # feature_f[i,:,:,:] = (x_f_ex[i,:,:,:,:] * W_f).sum(1)�   `   b                  for i in range(n):�   _   a          #            x_f_ex[:,j,:,:,:] = x_f�   ^   `                  for j in range(oc):�   ]   _          @        x_f_ex = numpy.zeros((n,oc,c,h,w),dtype=numpy.complex64)�   \   ^          A        feature_f = numpy.zeros((n,oc,h,w),dtype=numpy.complex64)�   [   ]           �   Z   \                  x_f = fft2(x)5�_�                    j       ����                                                                                                                                                                                                                                                                                                                            j          j          V       YS3     �   i   k          B        # y = numpy.tensordot(self.col, W, ((1, 2, 3), (1, 2, 3)))5�_�                    l       ����                                                                                                                                                                                                                                                                                                                            l          n          v       YS;     �   m   o          )        # return numpy.rollaxis(y, 3, 1),�   l   n                  #     y += b�   k   m                  # if b is not None:5�_�                   p        ����                                                                                                                                                                                                                                                                                                                            p           r           v        YSB    �   q   s                  return feature ,�   p   r                      feature += b�   o   q                  if b is not None:5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       YS     �   �   �          ,        Wb_f = numpy.where(W_f.real>=0,1,-1)5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �          �          V       YS     �   �   �          P        # Wb_f = numpy.where(W_f.real>=0,1,-1) + numpy.where(W_f.imag>=0,1j,-1j)5�_�      	              K       ����                                                                                                                                                                                                                                                                                                                            K          K          V       YS     �   J   L          P        # Wb_f = numpy.where(W_f.real>=0,1,-1) + numpy.where(W_f.imag>=0,1j,-1j)5�_�                  	   L       ����                                                                                                                                                                                                                                                                                                                            L          L          V       YS    �   K   M          ,        Wb_f = numpy.where(W_f.real>=0,1,-1)5�_�                    o        ����                                                                                                                                                                                                                                                                                                                            o           r          v       YS>     �   n   p          	        #�   o   q                  # if b is not None:�   p   r                  #     feature += b�   q   s                  # return feature ,5��