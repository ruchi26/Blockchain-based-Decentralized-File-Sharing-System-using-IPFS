# Blockchain-based-File-Sharing-System
The aim is to share files in a peer to peer manner using a blockchain to ensure decentralization. 

<h2>METHODOLOGY</h2>

<h3>4.1 Creating the Blockchain</h3>

<h4>4.1.1 Block Structure</h4>
In Data Share, a single block in a blockchain has the following structure:<br><br>

 
The Block contains : <br>
<b>Block number</b> - Simply displays the index number of the block. Block 0 refers to the genesis block.<br>
<b>Timestamp</b> - This field indicates as to when the block was created and added to the blockchain.  <br>
<b>Proof</b> - Also called a nonce, it stands for "number only used once," which is a number added to a hashed—or encrypted—block in a blockchain that, when rehashed, meets the difficulty level restrictions i.e by varying the proof we can vary the hash generated so that a new block can be created. <br>
<b>Previous hash</b> - This field represents the hash of the previous block. (In this case block index 2). The hash of the entire block is generated using the SHA-256 hashing algorithm. This field creates a chain of blocks and is the main element behind blockchain architecture’s security.<br>
<b>Sender</b> - The person who uploads the file enters his identity proof or name when he uploads the file.<br>
<b>Receiver</b> - Displays who the intended receiver of the shall be.<br>
<b>Hash of the file shared</b> - The uploaded file is first encrypted with the file key given by the uploader using the AES encryption mechanism and subsequently using the SHA-256 hashing algorithm when it is uploaded to ipfs. The hash, then received from the IPFS after the encryption is the hash of the shared file which is added to the block.<br>
 
<h4>4.1.2 Creating the Peer to Peer Network </h4>
In order to create a peer to peer network (p2p) for the blockchain to function, all the connected nodes must be in the same network. Only those users who are connected to the blockchain’s p2p network should have access to the blockchain’s data. This p2p network is created using  Socket Programming. We are working on a permissioned blockchains which require access to be a part of the blockchain. This access is granted when a user clicks on ‘Connect to the blockchain’ displayed on the home screen. Using socket programming, the list of connected nodes gets updated as soon as a new user gets connected or disconnected to the network and the updated list is broadcasted to the whole p2p  network. As soon as all the connected nodes get the updated list of the nodes in the network, the consensus protocol works smoothly whenever a new block is added or the blockchain gets updated. Thus, the peer to peer network works effectively.
 
<h4>4.1.3 File Key</h4>
The unique key/password shared between the sender and the receiver of the shared file to increase the security of the file(s) on the blockchain network.

The upload page is to be filled out by the uploader eager to share the file. The file key entered here will be used to encrypt the file using AES encryption before uploading it to the IPFS network. The uploader will have to share the key only with the intended receiver(s) so he/she can download the file. The type of files that can be uploaded are .pdf , .png , .jpeg and .txt. As of now the size of the file that can be uploaded to the network is limited to 16 Megabytes. 

The download page is to be filled by the receiver who has the valid file key shared by the sender and intends to download the shared file from the blockchain to his/her local computer. The file key here is used to decrypt: the AES encrypted file downloaded from the IPFS network so that the file can be interpretable. Make sure you enter the correct file key and hash for a successful download.
 
<h3>4.2 Integrating with IPFS</h3>
 
Our blockchain relies on IPFS for keeping it lightweight and scalable. If the files were stored directly on the blockchain, it would render the blockchain very heavy and inefficient. Combining IPFS and blockchain, we get to access the IPFS’s power of decentralized storage and enhance the blockchain’s security and accessibility. Instead of storing the file directly on the blockchain, we store the files on the IPFS network while the blockchain stores only the file’ hash. Each file will have a unique hash as IPFS employs the SHA-256 hashing algorithm. Thus, the file is stored in a secure decentralized network and is easily accessible through the blockchain. The file can be retrieved using its generated hash easily. Hence IPFS eliminates the bottleneck of storing entire files on the blockchain.
 
 
<h3>4.3 Using Cryptographic Encryption</h3>
<h4>4.3.1 SHA-256 Hashing Algorithm</h4>

We use the SHA-256 algorithm to generate a unique hash of the entire block that is used by the corresponding blocks to form the chain (via the previous hashes). IPFS as well uses this algorithm to generate the hash of the shared file. The SHA-256 hashing algorithm is employed because of the following advantages:
One-way:- Once the hash is generated, we can’t revert to the original data from the hash.
Deterministic:- For a particular input, the hash generated, always remains the same i.e. same input always gives the same hash.
Quick computation of the hash.
Avalanche-effect:- Even a slight change in the input will bring about a large change in the final hash, making it untraceable
Withstand collisions:- There is a very rare chance that the hash generated for two different inputs will be the same. Think of it as a human fingerprint!<br><br>
<h4>4.3.2 AES Encryption</h4>
AES Encryption is a form of symmetric, cryptographic encryption that depends on a shared key between the sender and receiver to access any file (here the file key) . If we had not employed the AES encryption, any connected user to the blockchain can access the file hash and thus, the shared file using the hash, directly from the IPFS. Using the AES Encryption, we encrypt the file using the file key of the uploader. Thus, if any user tries to download the file directly from the IPFS, all they get is a non-readable file. Thus, only users with a valid file key can access the readable file contents, thereby enhancing the security of the blockchain and the file contents.


<h2>RESULT</h2>

To test our application, we ran two instances of  Data Share on the computer locally at different ports, which served as two different and independent nodes (let’s say node A and node B). From both of them, we connected to the blockchain network and shared files using file keys.
From node A, we uploaded a file ‘x’ using file key ‘P’. 
We then downloaded the file ‘x’  from node B using the same key P’.
Subsequently, we uploaded a file ‘y’ from node B using file key ‘Q’ and downloaded the file ‘y’ from node ‘A’ using the file key ‘Q’
After the consequent sharing of the two files, the blockchain was updated at both the nodes.


