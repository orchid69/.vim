Vim�UnDo� ʅ��r����ғ2V��Ia�{<�-]�=��   4   plt.figure(figsize=(20,10))                             YdKa    _�                             ����                                                                                                                                                                                                                                                                                                                                                             Ya     �         8    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya     �         8    �         8    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya.     �                mac_data3 = np.loadtxt('log/BinaryNetCifar10-BN-Adam/test_BinaryNetCifar10.log', comments='#', delimiter='  ')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya/     �                �# ac_data2 = np.loadtxt('log/SPBinaryConvNetCifar10-BN-Adam-spatial/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya/     �                �# ac_data4 = np.loadtxt('log/SPBinaryConvNetCifar10-BN-Adam-spectral-comp-cut/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya0     �                �# ac_data5 = np.loadtxt('log/SPBinaryConvNetCifar10-BN-Adam-spectral-real-cut/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             Ya7     �   	      5    �   	   
   5    5�_�      	              
       ����                                                                                                                                                                                                                                                                                                                                                             Ya:     �   	      6      �ac_data7 = np.loadtxt('log/SPBinaryConvNetCifar10-BN-Adam-spectral-comp-full-restore/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�      
           	   
   #    ����                                                                                                                                                                                                                                                                                                                                                             Ya]     �   	      6      �ac_data8 = np.loadtxt('log/SPBinaryConvNetCifar10-BN-Adam-spectral-comp-full-restore/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�   	              
   
   .    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �   	      6      �ac_data8 = np.loadtxt('log/SPConvNetCifar10-BN-Adam-spectral-comp-full-restore/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�   
                 
   K    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �   	      6      �ac_data8 = np.loadtxt('log/SPConvNetCifar10-Adam-spectral-comp-full-restore/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�                    
   P    ����                                                                                                                                                                                                                                                                                                                                                             Ya�    �   	      6      �ac_data8 = np.loadtxt('log/SPConvNetCifar10-Adam-spcorrect-spatial/test_SPBinaryConvNetCifar10.log', comments='#', delimiter='  ')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �                {# plt.plot(np.arange(1,21), ac_data4[:,1], '--x', label = "FDBNN(Spectral comp cut)", color="g", linewidth=2, markersize=7)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �                {# plt.plot(np.arange(1,21), ac_data5[:,1], '--D', label = "FDBNN(Spectral real cut)", color="r", linewidth=2, markersize=7)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �         4    �         4    5�_�                       !    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �         5      xplt.plot(np.arange(1,21), ac_data7[:,1], '--x', label = "FDBNN(Spectral Restore)", color="g", linewidth=2, markersize=7)5�_�                       ,    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �         5      xplt.plot(np.arange(1,21), ac_data8[:,1], '--x', label = "FDBNN(Spectral Restore)", color="g", linewidth=2, markersize=7)5�_�                       ;    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �         5      xplt.plot(np.arange(1,21), ac_data8[:,1], '--+', label = "FDBNN(Spectral Restore)", color="g", linewidth=2, markersize=7)5�_�                       O    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �         5      xplt.plot(np.arange(1,21), ac_data8[:,1], '--+', label = "FDCNN(Spectral Restore)", color="g", linewidth=2, markersize=7)5�_�                       Q    ����                                                                                                                                                                                                                                                                                                                                                             Ya;    �         5      oplt.plot(np.arange(1,21), ac_data8[:,1], '--+', label = "FDCNN(Spatial)", color="g", linewidth=2, markersize=7)5�_�                    *        ����                                                                                                                                                                                                                                                                                                                                                             YaD     �   )   *          {# plt.plot(np.arange(1,21), ac_data4[:,0], '--x', label = "FDBNN(Spectral comp cut)", color="g", linewidth=2, markersize=7)5�_�                    *        ����                                                                                                                                                                                                                                                                                                                                                             YaD     �   )   *          {# plt.plot(np.arange(1,21), ac_data5[:,0], '--D', label = "FDBNN(Spectral real cut)", color="r", linewidth=2, markersize=7)5�_�                    )        ����                                                                                                                                                                                                                                                                                                                                                             YaE     �   )   +   3    �   )   *   3    5�_�                    *   %    ����                                                                                                                                                                                                                                                                                                                                                             YaJ    �   )   +   4      oplt.plot(np.arange(1,21), ac_data8[:,1], '--+', label = "FDCNN(Spatial)", color="r", linewidth=2, markersize=7)5�_�                       R    ����                                                                                                                                                                                                                                                                                                                                                             Ya�     �         4      pplt.plot(np.arange(1,21), ac_data6[:,1], '--^', label = "FDBNN(Spectral)", color="k", linewidth=2, markersize=7)5�_�                    (   R    ����                                                                                                                                                                                                                                                                                                                                                             Ya�    �   '   )   4      pplt.plot(np.arange(1,21), ac_data6[:,0], '--^', label = "FDBNN(Spectral)", color="k", linewidth=2, markersize=7)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        YdK.     �                plt.figure(figsize=(20,10))5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        YdK3     �         4      subplot1 = plt.subplot(1,2,1)5�_�                    #       ����                                                                                                                                                                                                                                                                                                                            #          0          v       YdK=    �   /   1          plt.tick_params(labelsize=18)�   .   0          plt.title("Loss")�   -   /          #plt.legend(loc='best', fontsize=18)�   ,   .          plt.ylabel("Loss", fontsize=18)�   +   -           plt.xlabel("epoch", fontsize=18)�   *   ,           �   )   +          oplt.plot(np.arange(1,21), ac_data8[:,0], '--+', label = "FDCNN(Spatial)", color="r", linewidth=2, markersize=7)�   (   *          xplt.plot(np.arange(1,21), ac_data7[:,0], '--x', label = "FDBNN(Spectral Restore)", color="g", linewidth=2, markersize=7)�   '   )          pplt.plot(np.arange(1,21), ac_data6[:,0], '--^', label = "FDBNN(Spectral)", color="m", linewidth=2, markersize=7)�   &   (          mplt.plot(np.arange(1,21), ac_data3[:,0], '--v', label = "BNN(Spatial)", color="b", linewidth=2, markersize=7)�   %   '          oplt.plot(np.arange(1,21), ac_data[:,0], '--o', label = "Normal(Spatial)", color="k", linewidth=2, markersize=7)�   $   &           �   #   %          subplot1.grid()�   "   $          subplot2 = plt.subplot(1,2,2)5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        YdK^     �                # plt.figure(figsize=(20,10))5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        YdK`    �         4      plt.figure(figsize=(20,10))5��